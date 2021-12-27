# GUI_Wrapper
A wrapper for the tkinter package of graphic utility functions.

While working on Graphic User Interfaces for Python modules in my other repositories, I felt a need for a simpler and more intuitive interface to the Tkinter package of graphics utility functions.  By simpler, I mean more meaningful names for function and parameters and fewer parameters to choose from -- just those most commonly used.

This is not to say that Tkinter isn't useful or even intuitive for others.  I respect that.  However, for my own use, I wanted a collection of interfaces that I have an easier time remembering and working with.

To this end, I set out to create my own "wrapper" for Tkinter.  This is my first attempt to write a wrapper, and I was surprised to find that doing so is more complicated than I had imagined.  It is not just a matter of more intuitive (to me) names for functions.  There is also the matter of filtering parameters and passing through the ones that I want to accept.

The overall process looks like this:
    calling program-->wrapper-->Tkinter function
    
To implement this, I took advantage of the **kwargs feature to allow optional parameters and the exec operator to execute a string that is built by the filter function as it checks each parameter.  The general approach is to filter the parameters being passed  to the wrapper and flag any that are not allowed while passing the others through to Tkinter.

The GUI_Wrapper is intended to be imported by any module that wants a GUI as its front end.
