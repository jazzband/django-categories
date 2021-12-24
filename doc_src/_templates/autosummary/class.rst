.. rst-class:: h4 text-secondary

{{ fullname }}

{{ objname | escape | underline}}

.. currentmodule:: {{ module }}

.. autoclass:: {{ objname }}

   {% block methods %}
   {% if methods %}
   .. rubric:: {{ _('Methods') }}

   .. autosummary::
   {% for item in methods %}
      {%- if "__" not in item %}
      ~{{ name }}.{{ item }}
      {% endif -%}
   {%- endfor %}
   {% endif %}
   {% endblock %}

   {% block attributes %}
   {% if attributes %}
   .. rubric:: {{ _('Attributes') }}

   .. autosummary::
   {% for item in attributes %}
      {%- if "__" not in item %}
      ~{{ name }}.{{ item }}{% endif %}
      {% endfor -%}
   {% endif %}
   {% endblock %}
