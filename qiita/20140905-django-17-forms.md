
# エラー処理# 


# add_error() #

- https://docs.djangoproject.com/en/dev/releases/1.7/#form-add-error

Improvements to Form error handling¶
Form.add_error()
Previously there were two main patterns for handling errors in forms:

Raising a ValidationError from within certain functions (e.g. Field.clean(), Form.clean_<fieldname>(), or Form.clean() for non-field errors.)
Fiddling with Form._errors when targeting a specific field in Form.clean() or adding errors from outside of a “clean” method (e.g. directly from a view).
Using the former pattern was straightforward since the form can guess from the context (i.e. which method raised the exception) where the errors belong and automatically process them. This remains the canonical way of adding errors when possible. However the latter was fiddly and error-prone, since the burden of handling edge cases fell on the user.

The new add_error() method allows adding errors to specific form fields from anywhere without having to worry about the details such as creating instances of django.forms.utils.ErrorList or dealing with Form.cleaned_data. This new API replaces manipulating Form._errors which now becomes a private API.

See Cleaning and validating fields that depend on each other for an example using Form.add_error().

# メタデータ #

- https://docs.djangoproject.com/en/dev/releases/1.7/#error-metadata

Error metadata
The ValidationError constructor accepts metadata such as error code or params which are then available for interpolating into the error message (see Raising ValidationError for more details); however, before Django 1.7 those metadata were discarded as soon as the errors were added to Form.errors.

Form.errors and django.forms.utils.ErrorList now store the ValidationError instances so these metadata can be retrieved at any time through the new Form.errors.as_data method.

The retrieved ValidationError instances can then be identified thanks to their error code which enables things like rewriting the error’s message or writing custom logic in a view when a given error is present. It can also be used to serialize the errors in a custom format such as XML.

The new Form.errors.as_json() method is a convenience method which returns error messages along with error codes serialized as JSON. as_json() uses as_data() and gives an idea of how the new system could be extended.

# エラーコンテナ #

- https://docs.djangoproject.com/en/dev/releases/1.7/#error-containers-and-backward-compatibility



Error containers and backward compatibility
Heavy changes to the various error containers were necessary in order to support the features above, specifically Form.errors, django.forms.utils.ErrorList, and the internal storages of ValidationError. These containers which used to store error strings now store ValidationError instances and public APIs have been adapted to make this as transparent as possible, but if you’ve been using private APIs, some of the changes are backwards incompatible; see ValidationError constructor and internal storage for more details.
