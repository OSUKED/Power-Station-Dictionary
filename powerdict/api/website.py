import os
import yaml
from loguru import logger
from typing import Optional
from fastapi import APIRouter, Depends, Request, HTTPException
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv
import markdown2

from powerdict.api import authentication
from powerdict import schemas, db, dictionary


load_dotenv()
static_dir = os.environ["STATIC_DIR"]
database_name = os.environ["DATABASE_NAME"]
database_dialect = os.environ["DATABASE_DIALECT"]
root_url = os.environ["ROOT_URL"]

db_client = db.get_db_client(
    database_name=database_name,
    dialect=database_dialect,
)

router = APIRouter(tags=["Website"])
templates = Jinja2Templates(directory=f'{static_dir}/templates')


@router.get("/")
async def home(
    request: Request,
):
    template_kwargs = {
        "content": markdown2.markdown("""# Welcome to the Power Station Dictionary!

> The *Power Station Dictionary* is a site that enables mapping between various power plant ids and automatically extracts data relating to those plants from Frictionless Data packages."""), 
        "request": request
    }

    return templates.TemplateResponse("home.jinja", template_kwargs)


def extract_frontmatter_and_content(markdown_content: str):
    frontmatter = None
    content = ""

    if markdown_content.startswith("---"):
        frontmatter_end = markdown_content.find("---", 3)
        if frontmatter_end != -1:
            try:
                frontmatter = yaml.safe_load(markdown_content[:frontmatter_end])
                content = markdown_content[frontmatter_end + 3:].strip()
            except yaml.YAMLError:
                pass

    if frontmatter is None:
        content = markdown_content.strip()

    return frontmatter, content


def load_blog_post(blog_id: str):
    file_path = os.path.join(f'{static_dir}/blogs', f'{blog_id}.md')
    logger.warning(file_path)

    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail=f"Blog post not found: '{blog_id}'")

    with open(file_path, 'r') as f:
        markdown_content = f.read()

    frontmatter, content = extract_frontmatter_and_content(markdown_content)
    html_content = markdown2.markdown(content)

    return {"blog_id": blog_id, "content": html_content, "frontmatter": frontmatter}


def load_blog_posts(
    blog_post_ids: Optional[list[str]] = None
):
    if blog_post_ids is not None:
        blog_posts = [load_blog_post(blog_post_id) for blog_post_id in blog_post_ids]
        return blog_posts
    
    blog_posts = []

    for filename in os.listdir(f'{static_dir}/blogs'):
        blog_posts.append(load_blog_post(filename.strip('.md')))

    return blog_posts

@router.get("/blog")
async def get_blog_home(request: Request):
    blog_posts = [
        {
            "blog_title": blog_post["frontmatter"]["title"],
            "blog_content": markdown2.markdown(" ".join(blog_post["content"].split()[:150]) + f" ... [Read More]({root_url}/blog/{blog_post['blog_id']})")
        }
        for blog_post 
        in load_blog_posts()
    ]
    
    return templates.TemplateResponse("blogs.jinja", {"request": request, "blog_posts": blog_posts})


@router.get("/blog/{blog_id}")
async def get_blog(
    request: Request,
    blog_id: str
):
    blog_post = load_blog_post(blog_id)
    blog_post_html = markdown2.markdown(blog_post["content"])

    template_kwargs = {
        "blog_title": blog_post["frontmatter"]["title"], 
        "blog_content": blog_post_html, 
        "request": request
    }

    return templates.TemplateResponse("blog.jinja", template_kwargs)


@router.get("/asset/{asset_id}")
async def get_asset(request: Request, asset_id: int):
    source_links = db_client.get_all('dict__source_link')
    asset = dictionary.load_site_data(asset_id, db_client, source_links)
    return templates.TemplateResponse("asset.jinja", {"request": request, "asset": asset})
