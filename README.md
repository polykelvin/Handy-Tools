# Handy-Tools

## Remove All PIP installation in current environment
To uninstall all packages installed via `pip`, you need to execute a command that iterates through each installed package and removes them. The **removeAllpip** is a way to do it, it has **ps1** for **window** and **sh** for **linux/mac**. 

**Important Considerations**:
- This will uninstall **all** Python packages that were installed via `pip`, which might include packages that are essential for certain applications or services on your system. Make sure you understand the implications of this, especially if you are working in a shared or production environment.
- If you have multiple Python environments (e.g., virtual environments), this command will only affect the currently active environment.
- After uninstallation, you might want to reinstall some essential packages or create a new environment if you're working with virtual environments.
