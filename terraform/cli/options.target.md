# `-target`

## `-target=ADDRESS`

Instructs Terraform to focus its planning efforts only on resource instances 
which match the given address and on any objects that those instances depend on.

Note: Use -target=ADDRESS in exceptional circumstances only, 
such as recovering from mistakes or working around Terraform limitations. 
Refer to [Resource Targeting](https://www.terraform.io/cli/commands/plan#resource-targeting) for more details.



## `-target=resource`

Limit the planning operation to only the given module, resource, or resource instance and all of its dependencies. 

You can use this option multiple times to include more than one object. 
This is for exceptional use only.
