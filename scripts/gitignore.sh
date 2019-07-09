################################################################################
# download output from gitignore and append it to content

_content+="\
################################################################################
# gitignore"

_ignored_items=(
    macos
    visualstudiocode
)

_ignored_items="${_ignored_items[@]}"
_content+="$(curl -L -s https://www.gitignore.io/api/${_ignored_items// /,})\n"



################################################################################
# append custom

_content+="\n\n\n\
################################################################################
# Custom

/custom/

.vscode/"



################################################################################
# print to console for piping

echo "${_content}"
