cd git-practice-04
git branch -r
git checkout -b ready1 origin/ready1
git checkout -b ready2 origin/ready2
git checkout -b ready3 origin/ready3
git checkout -b update1 origin/update1
git checkout -b update2 origin/update2
git branch -D main
git checkout -b main origin/main

git checkout main
git merge ready1
git commit -m "update"
git merge ready2
git commit -m "update"
git merge ready3
git merge -m "update"
git branch -D ready1 ready2 ready3

git checkout update1
git merge main
git merge -m "update"
git checkout update2
git merge main
git merge -m "update"
