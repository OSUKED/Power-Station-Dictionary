---
hide:
  - toc
---

# {{ package_elements.title }}

{% if package_elements['homepage'] != false  %}[Homepage]({{package_elements.homepage}}){% endif %}

{% if package_elements['description'] != false  %}{{package_elements.description}}{% endif %}

{% if package_elements['metadata'] != false  %}<br>
**Additional Metadata**

{{package_elements.metadata}}{% endif %}

{% if package_elements.resource_elements|length > 1 %}<br>
<br>
<br>

### Resources{% endif %}

{% for resource in package_elements.resource_elements %}
{% if package_elements.resource_elements|length > 1 %}##### {{resource.title}}{% endif %}

{% if resource['description'] != false  %}{{resource.description}}{% endif %}

<br>
**Fields**

{{resource['fields']}}

<br>

[Download]({{resource['download_url']}}){ .md-button }

<br>
{% endfor %}