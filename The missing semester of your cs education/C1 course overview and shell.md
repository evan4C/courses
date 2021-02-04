# C1 Course overview + the shell

## What is the shell?

Computers these days have a variety of interfaces for giving them commands; fancyful graphical user interfaces, voice interfaces, and even AR/VR are everywhere. These are great for 80% of use-cases, but they are often fundamentally restricted in what they allow you to do — you cannot press a button that isn’t there or give a voice command that hasn’t been programmed. To take full advantage of the tools your computer provides, we have to go old-school and drop down to a **textual interface**: The Shell.

While they may vary in the details, at their core they are all roughly the same: they allow you to run programs, give them input, and inspect their output in a semi-structured way.

In this lecture, we will focus on the **Bourne Again SHell**, or “bash” for short. This is one of the most widely used shells, and its syntax is similar to what you will see in many other shells. To open a shell *prompt* (where you can type commands), you first need a *terminal*. Your device probably shipped with one installed, or you can install one fairly easily.

## Using the shell

When you launch your terminal, you will see a *prompt* that often looks a little like this:

```bash
lifan@lifandeMacBook-Pro ~ %
```

This is the main textual interface to the shell. It tells you that you are on the machine `lifandeMacBook-Pro` and that your “current working directory”, or where you currently are, is `~` (short for “home”). The `%` tells you that you are not the root user (more on that later). At this prompt you can type a *command*, which will then be interpreted by the shell. The most basic command is to execute a program:

```bash
lifan@lifandeMacBook-Pro ~ % date
Thu Dec 31 14:57:41 JST 2020
```

Here, we executed the `date` program, which (perhaps unsurprisingly) prints the current date and time. The shell then asks us for another command to execute. We can also execute a command with *arguments*:

```bash
lifan@lifandeMacBook-Pro ~ % echo hello
hello
```

In this case, we told the shell to execute the program `echo` with the argument `hello`. The `echo` program simply **prints out its arguments**. The shell parses the command by splitting it by whitespace, and then runs the program indicated by the first word, supplying each subsequent word as an argument that the program can access. If you want to provide an argument that contains spaces or other special characters (e.g., a directory named “My Photos”), you can either quote the argument with `'` or `"` (`"My Photos"`), or escape just the relevant characters with `\` (`My\ Photos`).

But how does the shell know how to find the `date` or `echo` programs? Well, **the shell is a programming environment**, just like Python or Ruby, and so it has variables, conditionals, loops, and functions (next lecture!). When you run commands in your shell, you are really writing a small bit of code that your shell interprets. If the shell is asked to execute a command that doesn’t match one of its programming keywords, it consults an *environment variable* called `$PATH` that lists which directories the shell should search for programs when it is given a command:

```bash
lifan@lifandeMacBook-Pro ~ % echo $PATH
/Users/lifan/opt/anaconda3/bin:/Users/lifan/opt/anaconda3/condabin:/Library/Frameworks/Python.framework/Versions/3.8/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/Library/Apple/usr/bin
```

We can find out which file is executed for a given program name using the `which` program.

```bash
lifan@lifandeMacBook-Pro ~ % which echo
echo: shell built-in command
lifan@lifandeMacBook-Pro ~ % which pip
/Library/Frameworks/Python.framework/Versions/3.8/bin/pip
```

Or you can excute a command by using the absolute path.

```
lifan@lifandeMacBook-Pro ~ % /Library/Frameworks/Python.framework/Versions/3.8/bin/pip --version
pip 20.2.4 from /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages/pip (python 3.8)
```

## Navigating in the shell

A path on the shell is a delimited list of directories; separated by `/` on Linux and macOS and `\` on Windows. On Linux and macOS, the path `/` is the “root” of the file system, under which all directories and files lie. 

A path that starts with `/` is called an *absolute* path. Any other path is a *relative* path. Relative paths are relative to the current working directory, which we can see with the `pwd` (print working directory) command and change with the `cd` command. In a path, `.` refers to the current directory, and `..` to its parent directory:

```bash
lifan@lifandeMacBook-Pro ~ % pwd
/Users/lifan
lifan@lifandeMacBook-Pro ~ % cd /home
lifan@lifandeMacBook-Pro /home % cd ..
lifan@lifandeMacBook-Pro / % 
```

To see what lives in a given directory, we use the `ls` command:

```
lifan@lifandeMacBook-Pro ~ % ls
Desktop	Developer	Documents	Downloads
lifan@lifandeMacBook-Pro ~ % ls ..
Shared		lifan		self-discipline
```

两种快速切换目录的方法，一种是使用`~`来表示从根目录到对应目录的路径，另一种是使用`cd -`返回之前的目录

```
lifan@lifandeMacBook-Pro ~ % cd ~lifan/Desktop 
lifan@lifandeMacBook-Pro Desktop % cd -
~
lifan@lifandeMacBook-Pro ~ % 
```

Most commands accept flags and options (flags with values) that start with `-` to modify their behavior. Usually, running a program with the `-h` or `--help` flag will print some help text that tells you what flags and options are available. But in Mac if you type `ls --help`, it will return the following error, So it is recommended in Mac to use `man ls` to check the help document. It will open a new window that displays the details of the command. By pressing `q` you can quit the `man` window.

```
lifan@lifandeMacBook-Pro ~ % ls --help
ls: illegal option -- -
usage: ls [-@ABCFGHLOPRSTUWabcdefghiklmnopqrstuwx1%] [file ...]
```

One of the flags for `ls` command is `-l`, which will list files in long format and give you more information.

```bash
lifan@lifandeMacBook-Pro Test % ls -l
total 165856
drwxr-xr-x@ 3 lifan  staff        96 Mar  2  2020 Finance
-rw-r--r--@ 1 lifan  staff        62 Sep 22 22:09 README.md
-rw-r--r--@ 1 lifan  staff    332453 Dec 26 22:25 Screenshot.png
-rw-r--r--@ 1 lifan  staff  71086849 Dec 29 15:31 ellon musk.mp4
```

This gives us a bunch more information about each file or directory present. First, the `d` at the beginning of the line tells us that `Finance` is a directory. Then follow <u>three groups of three characters</u> (`rwx`). These indicate what permissions **the owner of the file** (`Finance`), **the owning group** (`staff`), and **everyone else** respectively have on the relevant item. A `-` indicates that the given principal does not have the given permission. Above, only the owner is allowed to modify (`w`) the `Finance` directory (i.e., add/remove files in it). To enter a directory, a user must have “search” (represented by “execute”: `x`) permissions on that directory (and its parents). To list its contents, a user must have read (`r`) permissions on that directory. For files, the permissions are as you would expect. Notice that nearly all the files in `/bin` have the `x`permission set for the last group, “everyone else”, so that anyone can execute those programs.

Some other handy programs to know about at this point are `mv` (to rename/move a file), `cp` (to copy a file), and `mkdir` (to make a new directory).

```bash
lifan@lifandeMacBook-Pro Test % mv README.md readyou.md
lifan@lifandeMacBook-Pro Test % ls
Finance		Screenshot.png	ellon musk.mp4	readyou.md
lifan@lifandeMacBook-Pro Test % cp readyou.md ../foo.md
lifan@lifandeMacBook-Pro Test % ls ..
Design		GitHub		Library		Literature	MATLAB		Personal	Test		Zoom		foo.md
lifan@lifandeMacBook-Pro Test % rm ../foo.md
lifan@lifandeMacBook-Pro Test % mkdir "new dir"
lifan@lifandeMacBook-Pro Test % ls
Finance		Screenshot.png	ellon musk.mp4	new dir		readyou.md
```

You can press `Ctrl + l` or type `clear` to clear up the shaell and return to first line

## Connecting programs

In the shell, programs have two primary “streams” associated with them: **their input stream** and **their output stream**. When the program tries to read input, it reads from the input stream, and when it prints something, it prints to its output stream. Normally, a program’s input and output are both your terminal. That is, your keyboard as input and your screen as output. However, we can also rewire those streams!

The simplest form of redirection is `< file` and `> file`. These let you rewire the input and output streams of a program to a file respectively. You can also use `>>` to **append** to a file.

```bash
lifan@lifandeMacBook-Pro Test % echo hello > hello.txt 
lifan@lifandeMacBook-Pro Test % cat hello.txt
hello
lifan@lifandeMacBook-Pro Test % cat < hello.txt > hello2.txt
lifan@lifandeMacBook-Pro Test % cat hello2.txt
hello
lifan@lifandeMacBook-Pro Test % cat < hello.txt >> hello2.txt
lifan@lifandeMacBook-Pro Test % cat hello2.txt               
hello
hello
```

> `cat` - print the content of a file

 Where this kind of input/output redirection really shines is in the use of *pipes*. The `|` operator lets you “chain” programs such that the output of one is the input of another:

```bash
lifan@lifandeMacBook-Pro Test % ls -l | tail -n 2
drwxr-xr-x  2 lifan  staff        64 Dec 31 17:01 new dir
-rw-r--r--@ 1 lifan  staff        62 Sep 22 22:09 readyou.md
lifan@lifandeMacBook-Pro Test % curl --head --silent google.com | grep -i content-length
Content-Length: 219
```

> `tail` - print the last **n** lines
>
> `curl` - transfer a URL
>
> ​             --head Fetch the headers only!
>
> ​             --silent Silent or quiet mode. Don't show progress meter or error messages.
>
> `grep -i` - search in a input stream for a given keyword

## A versatile and powerful tool

On most Unix-like systems, one user is special: the “root” user. You may have seen it in the file listings above. The root user is above (almost) all access restrictions, and can create, read, update, and delete any file in the system. You will not usually log into your system as the root user though, since it’s too easy to accidentally break something. Instead, you will be using the `sudo` command. As its name implies, it lets you “do” something “as su” (short for “super user”, or “root”). When you get permission denied errors, it is usually because you need to do something as root. Though make sure you first double-check that you really wanted to do it that way!

One thing you need to be root in order to do is writing to the `sysfs` file system mounted under `/sys`. `sysfs` exposes a number of kernel parameters as files, so that you can easily reconfigure the kernel on the fly without specialized tools. **Note that sysfs does not exist on Windows or macOS.**

## Exercises

One thing you need to be root in order to do is writing to the `sysfs` file system mounted under `/sys`. `sysfs` exposes a number of kernel parameters as files, so that you can easily reconfigure the kernel on the fly without specialized tools. **Note that sysfs does not exist on Windows or macOS.**

For example, the brightness of your laptop’s screen is exposed through a file called `brightness` under

```
/sys/class/backlight
```

By writing a value into that file, we can change the screen brightness. Your first instinct might be to do something like:

```
$ sudo find -L /sys/class/backlight -maxdepth 2 -name '*brightness*'
/sys/class/backlight/thinkpad_screen/brightness
$ cd /sys/class/backlight/thinkpad_screen
$ sudo echo 3 > brightness
An error occurred while redirecting file 'brightness'
open: Permission denied
```

This error may come as a surprise. After all, we ran the command with `sudo`! This is an important thing to know about the shell. Operations like `|`, `>`, and `<` are done *by the shell*, not by the individual program. `echo` and friends do not “know” about `|`. They just read from their input and write to their output, whatever it may be. In the case above, the *shell* (which is authenticated just as your user) tries to open the brightness file for writing, before setting that as `sudo echo`’s output, but is prevented from doing so since the shell does not run as root. Using this knowledge, we can work around this:

```
$ echo 3 | sudo tee brightness
```

Since the `tee` program is the one to open the `/sys` file for writing, and *it* is running as `root`, the permissions all work out. You can control all sorts of fun and useful things through `/sys`, such as the state of various system LEDs (your path might be different):

```
$ echo 1 | sudo tee /sys/class/leds/input6::scrolllock/brightness
```

# Next steps

At this point you know your way around a shell enough to accomplish basic tasks. You should be able to navigate around to find files of interest and use the basic functionality of most programs. In the next lecture, we will talk about how to perform and automate more complex tasks using the shell and the many handy command-line programs out there.

# Exercises

1. For this course, you need to be using a Unix shell like Bash or ZSH. If you are on Linux or macOS, you don’t have to do anything special. To make sure you’re running an appropriate shell, you can try the command `echo $SHELL`. If it says something like `/bin/bash` or `/usr/bin/zsh`, that means you’re running the right program.

   ```
   lifan@lifandeMacBook-Pro Test % echo $SHELL
   /bin/zsh
   ```

2. Create a new directory called `missing` under `/tmp`.

   ```
   lifan@lifandeMacBook-Pro Test % mkdir -p temp/missing
   ```

3. Look up the `touch` program. The `man` program is your friend.

4. Use `touch` to create a new file called `semester` in `missing`.

   ```
   lifan@lifandeMacBook-Pro Test % touch temp/missing/semester
   lifan@lifandeMacBook-Pro Test % ls temp/missing 
   semester
   ```

5. Write the following into that file, one line at a time:

   ```
   #!/bin/sh
   curl --head --silent https://missing.csail.mit.edu
   ```

   The first line might be tricky to get working. It’s helpful to know that `#` starts a comment in Bash, and `!` has a special meaning even within double-quoted (`"`) strings. Bash treats single-quoted strings (`'`) differently: they will do the trick in this case. See the Bash [quoting](https://www.gnu.org/software/bash/manual/html_node/Quoting.html) manual page for more information.

   ```
   lifan@lifandeMacBook-Pro Test % echo '#!/bin/sh' > temp/missing/semester                         
   lifan@lifandeMacBook-Pro Test % echo 'curl --head --silent https://missing.csail.mit.edu' >> temp/missing/semester
   lifan@lifandeMacBook-Pro Test % cat temp/missing/semester                                          
   #!/bin/sh
   curl --head --silent https://missing.csail.mit.edu
   ```

6. Try to execute the file, i.e. type the path to the script (`./semester`) into your shell and press enter. Understand why it doesn’t work by consulting the output of `ls` (hint: look at the permission bits of the file).

   ```
   lifan@lifandeMacBook-Pro Test % ./temp/missing/semester
   zsh: permission denied: ./temp/missing/semester
   lifan@lifandeMacBook-Pro Test % ls -l ./temp/missing/         
   total 8
   -rw-r--r--  1 lifan  staff  61 Dec 31 18:11 semester
   ```

7. Run the command by explicitly starting the `sh` interpreter, and giving it the file `semester` as the first argument, i.e. `sh semester`. Why does this work, while `./semester` didn’t?

   ```
   lifan@lifandeMacBook-Pro Test % sh ./temp/missing/semester
   HTTP/2 200 
   server: GitHub.com
   content-type: text/html; charset=utf-8
   last-modified: Mon, 28 Dec 2020 16:40:39 GMT
   access-control-allow-origin: *
   etag: "5fea0a87-1e9f"
   expires: Wed, 30 Dec 2020 01:22:39 GMT
   cache-control: max-age=600
   x-proxy-cache: MISS
   x-github-request-id: ECEC:729A:90CF8E:B3CC52:5FEBD407
   accept-ranges: bytes
   date: Thu, 31 Dec 2020 09:15:52 GMT
   via: 1.1 varnish
   age: 0
   x-served-by: cache-tyo19945-TYO
   x-cache: HIT
   x-cache-hits: 1
   x-timer: S1609406153.640427,VS0,VE177
   vary: Accept-Encoding
   x-fastly-request-id: 6579493e20d8035ad987feca25a0df464cca4d14
   content-length: 7839
   ```

8. Look up the `chmod` program (e.g. use `man chmod`).

9. >  **chmod** -- change file modes or Access Control Lists

10. Use `chmod` to make it possible to run the command `./semester` rather than having to type `sh semester`. How does your shell know that the file is supposed to be interpreted using `sh`? See this page on the [shebang](https://en.wikipedia.org/wiki/Shebang_(Unix)) line for more information.

    ```bash
    lifan@lifandeMacBook-Pro Test % chmod +x ./temp/missing/semester
    lifan@lifandeMacBook-Pro Test % ls -l ./temp/missing/semester
    -rwxr-xr-x@ 1 lifan  staff  61 Dec 31 18:15 ./temp/missing/semester
    ```

11. Use `|` and `>` to write the “last modified” date output by `semester` into a file called `last-modified.txt` in your home directory.

    ```bash
    lifan@lifandeMacBook-Pro Test % ./temp/missing/semester | grep -i last-modified > last-modified.txt
    ```

    

