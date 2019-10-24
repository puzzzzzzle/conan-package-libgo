# conan-package-libgo
```
To configure Conan client to work with Bintray, you will need to add Bintray repository to the list of remotes. To add Bintray conan repository, use the following command:
conan remote add <REMOTE> https://api.bintray.com/conan/puzzzzzzle1/khalidzhang 
And replace <REMOTE> with a name that identifies the repository (for example: "my-conan-repo"). 

To login use the conan user command:
conan user -p <APIKEY> -r <REMOTE> <USERNAME>
```
