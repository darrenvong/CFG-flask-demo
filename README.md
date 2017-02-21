## Flask Demo Examples

A collection of example Flask code written as demo in preparation for CF:G's Advanced Python course

## FAQs
**In my Command Prompt/Terminal, sometimes I see the following message:
`* Running on http://127.0.0.1:5000/`. So, why did you tell me to type `localhost:5000/[whatever_path_name]` instead in my browser?**

This is because `localhost` is "the same" as `127.0.0.1` - essentially, it is an easier, more human-readable version of the web address
pointing to the server you are running locally.

**Why do all of your template files end in `.htm.j2` rather than `.html`?**

This is purely done to make sure my template files are highlighted correctly with pretty and helpful colours in my text editor.
You may use either the `htm.j2` or `.html` file ending. As long you are referring to the templates by the same name when using
the `render_template` function, everything should work as expected.

For example, if you have a template called `hello.htm.j2` in the `templates` folder, write
```python
render_template("hello.htm.j2")
```

**Why is it that in the `hello` function, it reads `render_template("hello.htm.j2")`, whereas in the `hello_someone` function,
it reads `render_template("hello.htm.j2", name=name.title())` ?**

The `render_template` function accepts an unlimited number of **optional** named variables after the name of the template, which when passed to the `render_template` function, the data/value in the named variables themselves become accessible in the template files. This
is important as it allows **dynamic** data to be displayed without the need to write separate HTML templates for every possible name the user may type in through the browser.
