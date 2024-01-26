clean history: https://stackoverflow.com/questions/13716658/how-to-delete-all-commit-history-in-github
1.  Checkout
    `git checkout --orphan latest_branch`
2.  Add all the files
    `git add -A`
3.  Commit the changes
    `git commit -am "commit message"`
4.  Delete the branch
    `git branch -D main`
5.  Rename the current branch to main
    `git branch -m main`
6.  Finally, force update your repository
    `git push -f origin main`
    

PS: this will not keep your old commit history around


clean .git folder: https://stackoverflow.com/questions/5277467/how-can-i-clean-my-git-folder-cleaned-up-my-project-directory-but-git-is-sti

tagging
```console
git tag -a v1.4 -m "my version 1.4"
```
push tag
`git push origin --tags`

list tag
`git tag`

usuwanie tagow:
````console
git tag -d v1.4-lw
````
usuwanie tagow z remote:
```console
git push origin --delete <tagname>
```


przegladanie historii pliku
```
gitk --follow [filename]
```

graficzny podglad:
```
gitk
```


list tags with names:
```
git tag -l -n9
```


commit and stage at one step:
```
git commit -am "asdfasdf"
```


combining commits onto one commit
```
git rebase -i <commit>
```