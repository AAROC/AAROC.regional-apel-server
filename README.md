[![Build Status](https://travis-ci.org/AAROC/AAROC.regional-apel-server.svg?branch=master)](https://travis-ci.org/AAROC/AAROC.regional-apel-server)

# Role Name

Adds a [APEL](https://github.com/apel/apel) server service to your [Ansible Container](https://github.com/ansible/ansible-container) project. Run the following commands
to install the service:

```
# Set the working directory to your Ansible Container project root
$ cd myprojoect

# Install the service
$ ansible-container install AAROC.APEL-server
```

## Requirements

- [Ansible Container](https://github.com/ansible/ansible-container)
- An existing Ansible Container project. To create a project, simply run the following:
    ```
    # Create an empty project directory
    $ mkdir myproject

    # Set the working directory to the new directory
    $ cd myproject

    # Initialize the project
    $ ansible-contiainer init
    ```


## Role Variables

There are some default variables in `defaults` - take particular care to override the `version` of the apel server and ssm packages if you want test stuff.

## Dependencies

  - AAROC.certificates

## License

Apache-2.0

## Author Information

Bruce  Becker @brucellino

