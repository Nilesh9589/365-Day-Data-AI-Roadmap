In Python, indentation isn’t just for readability—it defines your code’s structure. Whenever you write a conditional (if/elif/else), loop (for/while), function or class, the lines that “belong” to that block must be indented the same amount. The interpreter uses those spaces to know which statements are grouped together.
  How it works

You write a header line ending with a colon (:)

Every line that’s part of that block sits under the header with extra spaces (usually 4)

When you outdent back to the previous level, you’re telling Python “this block is over”
x = 10
if x > 5:           # header line
    print("Big!")   # indented—inside the if-block
    x -= 1          # still inside the block
print("Done")       # back to no indent—outside the if-block


Use multiple ifs if you want all applicable conditions to run.

Use elif when you want only one branch to execute — the first matching one.

It’s not for computing values, but for controlling program flow.


try and except :
                if you think your code can blow up if user for example put number in input if asked for alphabet then you can use try there. make sure try block has only one line which you think can make code blow up because even if you put bunch of code lines in try it will move further even if first one fail it would jump to except.
 