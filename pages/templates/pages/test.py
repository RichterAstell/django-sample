<h1>test</h1>

{% if error_message %}<p><strong>{{ error_message }}</strong></p>{% endif %}

<form action="{% url 'pages:test' %}" method="post">
    {% csrf_token %}
    <input type="text" name="username" id="username" value="">
    <label for="username">user name</label>
    <br>
    <input type="password" name="password" id="password" value="">
    <label for="password">password</label>
    <br>
    <input type="submit" value="Login">
</form>