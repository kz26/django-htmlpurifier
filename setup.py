from distutils.core import setup, Extension


setup ( name = 'htmlpurifier',
        version = open('lib/__version__.py').readline().rstrip().split('=')[1].strip('"'),
        author = 'whitehat2k9',
        author_email = '',
        description = 'A silly but useful hack for sanitizing untrusted HTML input in Django forms via the PHP HTML Purifier library',
        package_dir = {'htmlpurifier': 'lib'},
        packages = ['htmlpurifier'],
        package_data = {'htmlpurifier': ['htmlpurifier-cli.php', 'readme.md',]},
        include_package_data=True,
       )
