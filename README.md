# GUI_Wrapper
A wrapper for the tkinter package of graphic utility functions.

While working on Graphic User Interfaces for Python modules in my other repositories, I felt a need for a simpler and more intuitive interface to the Tkinter package of graphics utility functions.  By simpler, I mean more meaningful names for function and parameters and fewer parameters to choose from -- just those most commonly used.

This is not to say that Tkinter isn't useful or even intuitive for others.  I respect that.  However, for my own use, I wanted a collection of interfaces that I have an easier time remembering and working with.

To this end, I set out to create my own "wrapper" for Tkinter.  This is my first attempt to write a wrapper, and I was surprised to find that doing so is more complicated than I had imagined.  It is not just a matter of more intuitive (to me) names for functions.  There is also the matter of filtering parameters and passing through the ones that I want to accept.

The overall process looks like this:
    calling program-->wrapper-->Tkinter function
    
To implement this, I took advantage of the **kwargs feature to allow optional parameters and the exec operator to execute a string that is built by the filter function as it checks each parameter.  The general approach is to filter the parameters being passed  to the wrapper and flag any that are not allowed while passing the others through to Tkinter.

The GUI_Wrapper is intended to be imported by any module that wants a GUI as its front end.

Update 1/14/2022

After working on the GUI_Wrapper for several days, I have come to the conclusion that creating a class for the wrapper is just making things more complicated, so I investigated other means of achieving the goals of simplicity and commonly used features.  I found a reasonable approach on Geeks-4-Geeks: a registration application that uses tkinter to set up a registration form for a student enrollment system.  This app can be easily tailored for other apps where a GUI interface for entering client information is needed.  It is well-documented and easy to follow.  While it doesn't used a class to encapsulate the GUI code, it allows for OO technology to link into the mainloop inside which the calls to tkinter are done.  This is done by binding responses to entry fields and buttons to functions written outside the mainloop().

I will start a different repository for the registration code and add to it as I make modifications for other apps requiring a GUI.

In the meantime, the work-to-date for writing a GUI_Wrapper class is included in this repository.  Anyone wishing to use and/or extend the wrapper is free to do so.
