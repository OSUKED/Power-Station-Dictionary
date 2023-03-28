# Documentation Generation



```python
#exports
import junix
import pandas as pd
from html.parser import HTMLParser
from nbdev.export2html import convert_md

import os
import codecs
from ipypb import track
from warnings import warn
```

<br>

### User Inputs

```python
docs_dir = '../docs'
img_dir = f'{docs_dir}/img/nbs'
dev_nbs_dir = '.'
```

<br>

### Converting Notebooks to Markdown

```python
#exports
def encode_file_as_utf8(fp):
    with codecs.open(fp, 'r') as file:
        contents = file.read(1048576)
        file.close()

        if not contents:
            pass
        else:
            with codecs.open(fp, 'w', 'utf-8') as file:
                file.write(contents)
            
def convert_nbs_to_md(nbs_dir, img_dir, docs_dir):
    nb_files = [f for f in os.listdir(nbs_dir) if f[-6:]=='.ipynb']

    for nb_file in track(nb_files):
        nb_fp = f'{nbs_dir}/{nb_file}'
        junix.export_images(nb_fp, img_dir)
        convert_md(nb_fp, docs_dir, img_path=f'{img_dir}/', jekyll=False)

        md_fp =  docs_dir + '/'+ nb_file.replace('.ipynb', '') + '.md'
        encode_file_as_utf8(md_fp)
```

```python
for nbs_dir in [dev_nbs_dir]:
    convert_nbs_to_md(nbs_dir, img_dir, docs_dir)
```


<div><span class="Text-label" style="display:inline-block; overflow:hidden; white-space:nowrap; text-overflow:ellipsis; min-width:0; max-width:15ex; vertical-align:middle; text-align:right"></span>
<progress style="width:60ex" max="7" value="7" class="Progress-main"/></progress>
<span class="Progress-label"><strong>100%</strong></span>
<span class="Iteration-label">7/7</span>
<span class="Time-label">[00:01<00:00, 0.18s/it]</span></div>


<br>

### Cleaning Markdown

```python
#exports
class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags = []
    
    def handle_starttag(self, tag, attrs):
        self.tags.append(self.get_starttag_text())

    def handle_endtag(self, tag):
        self.tags.append(f"</{tag}>")
        
get_substring_idxs = lambda string, substring: [num for num in range(len(string)-len(substring)+1) if string[num:num+len(substring)]==substring]

def convert_df_to_md(df):
    idx_col = df.columns[0]
    df = df.set_index(idx_col)
    
    if idx_col == 'Unnamed: 0':
        df.index.name = ''
    
    table_md = df.to_markdown()
    
    return table_md

def extract_div_to_md_table(start_idx, end_idx, table_and_div_tags, file_txt):
    n_start_divs_before = table_and_div_tags[:start_idx].count('<div>')
    n_end_divs_before = table_and_div_tags[:end_idx].count('</div>')

    div_start_idx = get_substring_idxs(file_txt, '<div>')[n_start_divs_before-1]
    div_end_idx = get_substring_idxs(file_txt, '</div>')[n_end_divs_before]

    div_txt = file_txt[div_start_idx:div_end_idx]
    potential_dfs = pd.read_html(div_txt)
    
    assert len(potential_dfs) == 1, 'Multiple tables were found when there should be only one'
    df = potential_dfs[0]
    md_table = convert_df_to_md(df)

    return div_txt, md_table

def extract_div_to_md_tables(md_fp):
    with open(md_fp, 'r') as f:
        file_txt = f.read()
        
    parser = MyHTMLParser()
    parser.feed(file_txt)

    table_and_div_tags = [tag for tag in parser.tags if tag in ['<div>', '</div>', '<table border="1" class="dataframe">', '</table>']]
    
    table_start_tag_idxs = [i for i, tag in enumerate(table_and_div_tags) if tag=='<table border="1" class="dataframe">']
    table_end_tag_idxs = [table_start_tag_idx+table_and_div_tags[table_start_tag_idx:].index('</table>') for table_start_tag_idx in table_start_tag_idxs]

    div_to_md_tables = []

    for start_idx, end_idx in zip(table_start_tag_idxs, table_end_tag_idxs):
        div_txt, md_table = extract_div_to_md_table(start_idx, end_idx, table_and_div_tags, file_txt)
        div_to_md_tables += [(div_txt, md_table)]
        
    return div_to_md_tables

def clean_md_file_tables(md_fp):
    div_to_md_tables = extract_div_to_md_tables(md_fp)
    
    with open(md_fp, 'r') as f:
        md_file_text = f.read()

    for div_txt, md_txt in div_to_md_tables:
        md_file_text = md_file_text.replace(div_txt, md_txt)

    with open(md_fp, 'w') as f:
        f.write(md_file_text)
        
    return
```

```python
md_files = [f for f in os.listdir(docs_dir) if f[-3:]=='.md']

for md_file in md_files:
    div_to_md_tables = clean_md_file_tables(md_file)
```


    ---------------------------------------------------------------------------

    FileNotFoundError                         Traceback (most recent call last)

    <ipython-input-9-749c5ee890cb> in <module>
          2 
          3 for md_file in md_files:
    ----> 4     div_to_md_tables = clean_md_file_tables(md_file)
    

    <ipython-input-8-2465abeb9526> in clean_md_file_tables(md_fp)
         61 
         62 def clean_md_file_tables(md_fp):
    ---> 63     div_to_md_tables = extract_div_to_md_tables(md_fp)
         64 
         65     with open(md_fp, 'r') as f:
    

    <ipython-input-8-2465abeb9526> in extract_div_to_md_tables(md_fp)
         41 
         42 def extract_div_to_md_tables(md_fp):
    ---> 43     with open(md_fp, 'r') as f:
         44         file_txt = f.read()
         45 
    

    FileNotFoundError: [Errno 2] No such file or directory: '00-documentation.md'

