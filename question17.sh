cd git-practice-03
git branch -r
git checkout -b branch1 
git checkout -b branch2
git checkout main

cd ./dir3
cp -i bar bar_copy
git add *
cd ../
git commit -m "add"

git checkout branch1
cd ./dir1/dir2
git mv foo ../
cd ../
git rm -r dir2
git add *
git commit -m "update"
cd ../
touch newfile1
git add *
git commit -m "update"

git checkout branch2
cd ./dir1/dir2
git mv foo foo_modified
git add *
git commit -m "update"
cd ../../dir3
git mv bar newfile2
git add *
git commit -m "update"
cd ../
git mv dir3 dir1
git commit -m "finnal update"

