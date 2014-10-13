Swift vs. C# : Access Control

# Modules and Source Files

Module: ビルド単位

> A module is a single unit of code distribution—a framework or application that is built and shipped as a single entity and that can be imported by another module with Swift’s import keyword.


Source File: *.swift 単位

> A source file is a single Swift source code file within a module (in effect, a single file within an app or framework). 

> Although it is common to define individual types in separate source files, a single source file can contain definitions for multiple types, functions, and so on.



# Access Levels


Public: 全解放

> Public access enables entities to be used within any source file from their defining module, and also in a source file from another module that imports the defining module. 

> You typically use public access when specifying the public interface to a framework.


Internal: モジュール内限定

> Internal access enables entities to be used within any source file from their defining module, but not in any source file outside of that module. 

> You typically use internal access when defining an app’s or a framework’s internal structure.

Private: 同じソースファイル限定

> Private access restricts the use of an entity to its own defining source file. 


> Use private access to hide the implementation details of a specific piece of functionality.


## Guiding Principle of Access Levels


Principal: より低いレベルのエンティティに関しては定義できない

> No entity can be defined in terms of another entity that has a lower (more restrictive) access level.

- private/inernalタイプは public で定義できな
- 引き数、返り値の型を上回るレベルの関数を定義できない




## Default Access Levels


- デフォルト internal 



## Access Levels for Single-Target Apps


## Access Levels for Frameworks



# Access Control Syntax

# Custom Types

## Tuple Types

## Function Types


## Enumeration Types


## Nested Types


# Subclassing

# Constants, Variables, Properties, and Subscripts


## Getters and Setters


# Initializers

## Default Initializers


## Default Memberwise Initializers for Structure Types

# Protocols

## Protocol Inheritance


## Protocol Conformance


# Extensions

## Adding Protocol Conformance with an Extension


# Generics

# Type Aliases




