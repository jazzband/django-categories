.. rst-class:: h4 text-secondary

{{ fullname }}

{{ objname | escape | underline}}
.. currentmodule:: {{ fullname }}


.. automodule:: {{ fullname }}

   {% block modules -%}
   {% if modules %}

   .. rubric:: Submodules

   .. autosummary::
      :toctree:
      :recursive:
   {% for item in modules %}
      {% if "migrations" not in item and "tests" not in item%}{{ item }}{% endif %}
   {%- endfor %}
   {% endif %}
   {% endblock %}
   {% block attributes -%}
   {%- if attributes -%}
   .. rubric:: {{ _('Module Attributes') }}

   .. autosummary::
      :toctree:
   {% for item in attributes %}
      {{ item }}
   {%- endfor -%}
   {%- endif -%}
   {% endblock attributes -%}
   {%- block functions -%}
   {%- if functions %}

   .. rubric:: {{ _('Functions') }}

   .. autosummary::
      :toctree:
   {% for item in functions %}
      {{ item }}
   {%- endfor -%}
   {%- endif -%}
   {% endblock functions -%}
   {% block classes -%}
   {% if classes %}

   .. rubric:: {{ _('Classes') }}

   .. autosummary::
      :toctree:
   {% for item in classes %}
      {{ item }}
   {%- endfor -%}
   {%- endif -%}
   {% endblock classes -%}
   {% block exceptions -%}
   {% if exceptions %}

   .. rubric:: {{ _('Exceptions') }}

   .. autosummary::
      :toctree:
   {% for item in exceptions %}
      {{ item }}
   {%- endfor -%}
   {%- endif -%}
   {% endblock exceptions -%}
