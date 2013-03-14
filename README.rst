0. Clone the rpdb repo::

   git clone https://github.com/AlexandreZani/rpdb.git

1. Clone the vim_rpdb repo::

   git clone https://github.com/AlexandreZani/vim_rpdb.git

2. Copy vim_rpdb/plugin/python_rpdb.vim into ~/.vim/plugin and vim_rpdb/python into ~/.vim/

3. Start the sample program::

   cd rpdb
   ./factor.py listening

4. Start vim::

   vim

5. Start the debugging session::

   :RpdbStart

6. Step through the sample program::

   :RpdbStep

7. Let the program finish::

   :RpdbContinue

8. See the beautiful crash.

9. Contibute bug reports, bug fixes, documentation, features and cookies...
