{% macro render_field(field) %}
<tr>
  <td>
    {{ field.label }}
    {% if field.errors %}
    <span class="errors">
      {% for error in field.errors %}
        {{ error + " " }} 
      {% endfor %}
    </span>
    {% endif %}
  </td>
</tr>
<tr>
  <td dir={{ dir }}>{{ field(class_='form-field') }}</td>
</tr>
{% endmacro %}

{% macro flasher() %}
  {% with messages = get_flashed_messages() %}
    {% if messages %}
    <div id="flasher">
      {% for msg in messages %}
        {{ msg + " " }}
      {% endfor %}
    </div>
    {% endif %}
  {% endwith %}
{% endmacro %}

