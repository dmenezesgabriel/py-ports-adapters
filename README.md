# Ports and Adapters or Hexagonal Architecture in Python

## Core

Contains the business logic of the application. It is independent of any framework or database.

### Domain

#### Entities

Contains the domain entities or models.

### Application

#### Ports

##### Entry Ports

Interfaces used for communication from the outside to the inside of the application. As an example, it can be a service.

##### Exit Ports

Interfaces used for communication from the inside to the outside of the application. As an example, it can be a repository.

#### Use Cases or Services

Contains the use cases or services of the application.

## Adapters

Contains the implementation of the interfaces defined in the core. It is dependent on the core and uses a framework or database.

### Drivers (Actors)

Are the ones that receive method calls from the outside of the application. As an example, it can be a web server.

### Driven (Actors)

Are the ones that receive method calls from the inside of the application. As an example, it can be a database.

#### Repositories

Are the ones with the goal of send and receive data from the database or other storage device.

#### Recipients

Are the ones with the goal of only send data and forget it like a message broker or SMTP server.

## Folder Structure

```sh
.
|____tests
|____app
| |____src
| | |____adapter
| | | |____driver
| | | | |____api
| | | | | |____api_v1
| | | | | | |____endpoints
| | | | | |____controllers
| | | |____driven
| | | | |____infra
| | | | | |____database
| | | | | | |____repositories
| | | | | | |____models
| | |____core
| | | |____domain
| | | | |____base
| | | | |____entities
| | | | |____value_objects
| | | |____application
| | | | |____services
| | | | |____ports
```

## Resources

- https://github.com/bobthemighty/python-ports-adapters
- https://github.com/jorzel/opentable
- https://github.com/pcieslinski/courses_platform
- https://github.com/evoludigit/clean_fastapi
- https://github.com/kurosouza/webshop
- https://medium.com/@surajit.das0320/understanding-unit-of-work-manager-bcdfb9190d86
