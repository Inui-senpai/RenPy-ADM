# Higher chance to survive after SDK update
# NOTE: Works only on launch!

init -2 python:
    import darkdetect

    if darkdetect.isDark():
        persistent.theme = "dark"
    else:
        persistent.theme = None
