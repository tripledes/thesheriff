.. The Sheriff documentation master file, created by
   sphinx-quickstart on Sat Nov 30 18:55:39 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to The Sheriff's documentation!
=======================================



Introduction
============

This part of the documentation is intended to birefly introduce
The Sheriff application.

.. toctree::
   introduction

Functionality - Application usage
=================================

Here's all you need to run and test The Sheriff application.

.. toctree::
    usage

Design - Hexagonal Architecture
===============================
Missing explanation of why we choose this architecture

- The Sheriff Application

Application contains the main use cases identified by the team and also auxiliary use cases:
List gangs, create a gang, create an outlaw, invite a friend, join a gang, list friends, list gangs, rate the raid and
send notifications.
On this layer we also put the request classes, that are created on the controller, containing all necessary
information to execute the use cases

- The Sheriff Domain

Here we put our domain classes (Outlaw, Gang and Raid) containing all pertinent business logic and the factory classes.

- The Sheriff Infraestructure

Contains the REST API endpoints and MySQL repositories

Tools
=====

.. toctree::
    tools

The API Documentation
=====================

If you are looking for information on a specific function, class, or method,
this part of the documentation is for you.

.. toctree::
   :maxdepth: 2

   application
   domain
   infrastructure
