# INSTRUCTIONS TO SETUP FORKED API VERSION

## STEPS
1. 
    1.a) If you want to download from my github (this will eventually be taken down), visit <a href=https://github.com/Huntermuze/RaspberryJuice>here</a>.
    1.b) Navigate to **/download_here**.

    2.a) If you are reading this, you likely have access to this repo. Hence, navigate to **/modified_api/API** and obtain the files from there.

2. Download both ``MC_Py_API.zip`` and ``RJ-Fork.jar``.

3. Go to your ``Minecraft Tools`` folder that was provided by the RMIT instructors.

4. Drag/drop and **replace** the current ``MC_Py_API.zip`` file with the newly downloaded one. Do not rename this file.

5. Navigate to ``server/plugins`` (you should be within your ``Minecraft Tools`` directory here).

6. Drag/drop and ``RJ-Fork.jar`` into there and **delete** ``raspberryjuice-1.12.1.jar``.

7. If on MAC open *Terminal* (may need elevated privalleges - use ``sudo`` in that case), and if on windows open up *Command Prompt*.

8. Type the following command and hit enter: ``pip uninstall mcpi``. Once its finished, close the window.

9. Go back to your ``Minecraft Tools`` folder, and run the ``Install_API`` script once again. Let that complete.

10. You're good to go! Start your server and your minecraft instance up and test out the new methods. The API should be a little faster too :).