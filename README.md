# Ports and Adapters or Hexagonal Architecture in Python

## Core

Contains the business logic of the application. It is independent of any framework or database.

### Domain

#### Entities

Contains the domain entities or models.

### Application

#### Ports

Interfaces for the use cases or services of the application.

#### Use Cases or Services

Contains the use cases or services of the application.

## Adapters

Contains the implementation of the interfaces defined in the core. It is dependent on the core and uses a framework or database.

### Drivers

It is the entry point of the application. It is dependent on the core and uses a framework or database. As an example, it can be a web server.

### Driven

It is the exit point of the application. It is dependent on the core and uses a framework or database. As an example, it can be a database.

## Folder Structure

```sh
.
|____tests
|____src
| |____adapter
| | |____driver
| | | |____api
| | | | |____controllers
| | | | | |____user_controller.py
| | | | |____program.py
| | |____driven
| | | |____infra
| | | | |____repositories
| | | | | |____user_repository.py
| | | | |____orm
| | | | | |____.gitkeep
| |____core
| | |____domain
| | | |____base
| | | | |____assertion_concern.py
| | | |____entities
| | | | |____user.py
| | | |____value_objects
| | | | |____.gitkeep
| | |____application
| | | |____services
| | | | |____user_service.py
| | | |____ports
| | | | |____user_service.py
| | | | |____user_repository.py
|____README.md
```
