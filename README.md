## Flask Demo Examples

A collection of example Flask code written as demo in preparation for CF:G's Advanced Python course

## FAQs

**Why is it that in the `hello` function, it reads `render_template("hello.html")`, whereas in the `hello_someone` function,
it reads `render_template("hello.html", name=name.title())` ?**

The `render_template` function accepts an unlimited number of **optional** named variables after the name of the template, which when passed to the `render_template` function, the data/value in the named variables themselves become accessible in the template files. This
is important as it allows **dynamic** data to be displayed without the need to write separate HTML templates for every possible name the user may type in through the browser.
