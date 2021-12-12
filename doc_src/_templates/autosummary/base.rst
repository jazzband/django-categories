.. rst-class:: h4 text-secondary

{{ fullname }}

{{ objname | escape | underline}}

.. currentmodule:: {{ module }}
{%- if not objname.startswith("test") %}
.. auto{{ objtype }}:: {{ objname }}
{%- endif %}
