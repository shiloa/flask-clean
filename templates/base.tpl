<!DOCTYPE html>
<html>
  <head>
    {% include "meta.tpl" %}
    <!-- some pretty fonts -->
    <!-- <link href='http://fonts.googleapis.com/css?family=Josefin+Sans+Std+Light' rel='stylesheet' type='text/css'> -->
    <!-- <link href='http://fonts.googleapis.com/css?family=Molengo' rel='stylesheet' type='text/css'> -->
    <link href='http://fonts.googleapis.com/css?family=Cantarell:regular,italic,bold,bolditalic' rel='stylesheet' type='text/css'>
    {% from "_formhelpers.tpl" import flasher %}
    <title>{% block title %}{% endblock %} </title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/base.css') }}" type="text/css" media="screen" charset="utf-8" />
    {% block stylesheets %}{% endblock %}
    <script src="{{ url_for('static', filename='js/jquery-1.4.2.min.js') }}" type="text/javascript" charset="utf-8"></script>
    {% include "analytics.tpl" %}
  </head>
  <body>
    <div id="content"> 
      {{ flasher() }}
      {# include "nav.tpl" #}
      <div id="main"> 
        {% block main %}{% endblock %}
      </div>
    </div>
    {# include "footer.tpl" #}
    {% block javascripts %}{% endblock %}
  </body>
</html>
