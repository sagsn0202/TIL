# 190108

### 단축어 만들기

`touch .bashrc`

`vim .bashrc`

`alias 'jn'='jupyter notebook'`

혹은

`echo 'alias "jn"="jupyter notebook"' >> .bashrc`



### git

`which git`: 시작하기 전

`git init`: (master) -> repository(저장소)

`rm -rf .git`



`vim .gitconfig`

```
[user]
    name = Eun Seok Hwang
    email = sagsn0202@naver.com
[core]
    editor = vim
    whitespace = off
    excludesfile = ~/.gitignore
[advice]
    statusuoption = false
[color]
    ui = true
[push]
    default = current
```

`cd .git`

`cat config`

```
sagsn0202:~/workspace/prj/.git (GIT_DIR!) $ cat config
[core]
        repositoryformatversion = 0
        filemode = true
        bare = false
        logallrefupdates = true
```



`git status`

`touch first_file.txt`

`git status`

```
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)

        first_file.txt

nothing added to commit but untracked files present (use "git add" to track)
```

`git add first_file.txt`

`git status`

```
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)

        new file:   first_file.txt
```



`git commit -m ''`

```
1. 현재형으로
2. 명령하듯이
3. 너무 길지 않게
```



`git remote add origin https://github.com/sagsn0202/learn_git_prj.git`

```
[core]
        repositoryformatversion = 0
        filemode = true
        bare = false
        logallrefupdates = true
[remote "origin"]
        url = https://github.com/sagsn0202/learn_git_prj.git
        fetch = +refs/heads/*:refs/remotes/origin/*
```

`git remote -v`

```
origin  https://github.com/sagsn0202/learn_git_prj.git (fetch)
origin  https://github.com/sagsn0202/learn_git_prj.git (push)
```



`git push -u origin master`

```
Username for 'https://github.com': sagsn0202
Password for 'https://sagsn0202@github.com':
```



 ``git clone https://github.com/sagsn0202/learn_git_prj.git ssafy_git`



`code .`



`git pull`



`git help`

```
usage: git [--version] [--help] [-C <path>] [-c name=value]
           [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
           [-p | --paginate | --no-pager] [--no-replace-objects] [--bare]
           [--git-dir=<path>] [--work-tree=<path>] [--namespace=<name>]
           <command> [<args>]

These are common Git commands used in various situations:

start a working area (see also: git help tutorial)
   clone      Clone a repository into a new directory
   init       Create an empty Git repository or reinitialize an existing one

work on the current change (see also: git help everyday)
   add        Add file contents to the index
   mv         Move or rename a file, a directory, or a symlink
   reset      Reset current HEAD to the specified state
   rm         Remove files from the working tree and from the index

examine the history and state (see also: git help revisions)
   bisect     Use binary search to find the commit that introduced a bug
   grep       Print lines matching a pattern
   log        Show commit logs
   show       Show various types of objects
   status     Show the working tree status

grow, mark and tweak your common history
   branch     List, create, or delete branches
   checkout   Switch branches or restore working tree files
   commit     Record changes to the repository
   diff       Show changes between commits, commit and working tree, etc
   merge      Join two or more development histories together
   rebase     Reapply commits on top of another base tip
   tag        Create, list, delete or verify a tag object signed with GPG

collaborate (see also: git help workflows)
   fetch      Download objects and refs from another repository
   pull       Fetch from and integrate with another repository or a local branch
   push       Update remote refs along with associated objects

'git help -a' and 'git help -g' list available subcommands and some
concept guides. See 'git help <command>' or 'git help <concept>'
to read about a specific subcommand or concept.
```

