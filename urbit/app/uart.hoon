/-  *uart
/+  default-agent, dbug
|%
+$  versioned-state
  $%  state-0
  ==
+$  state-0
  $:  [%0 name=@tas]
  ==
+$  card  card:agent:gall
--
%-  agent:dbug
=|  state-0
=*  state  -
^-  agent:gall
|_  =bowl:gall
+*  this     .
    default  ~(. (default-agent this %|) bowl)
++  on-init
  ^-  (quip card _this)
  :_  this
  [%pass /init %arvo %l %spin 'uart']
++  on-save   !>(state)
++  on-load
  |=  old=vase
  ^-  (quip card _this)
  `this(state !<(state-0 old))
++  on-poke
  |=  [=mark =vase]
  ^-  (quip card _this)
  ?>  ?=(%uart-action mark)
  =/  act  !<(action vase)
  ?-    -.act
      %read
    :_  this
    [%pass /spit/ %arvo %l %spit agent.act mark.act dat.act]~
    ==
::
++  on-peek
  |=  =path
  ^-  (unit (unit cage))
  ~&  >>  path
  =/  dev  `@tas`(snag 2 path)
  ?+  path  (on-peek:default path)
  ==
++  on-arvo
  |=  [=wire =sign-arvo]
  ^-  (quip card _this)
  =/  cmd    (snag 0 wire)
  =/  device  (snag 1 wire)
  =/  cad  +.sign-arvo
  ~&  >  ['wire' wire]
  ~&  >  ['sign-arvo' sign-arvo]
  ?+  cmd  (on-arvo:default wire sign-arvo)
      %getattr
    ?+  sign-arvo  (on-arvo:default wire sign-arvo)
      [%loch %seen *]
      =/  termio  (unpack-term:uart dat.sign-arvo)
      ~&  ['term' termio]
      :-  ~
        %_  this
          term  (~(put by term) device termio)
        ==
      ==
    ::
      %setattr
    [~ this]
    ::
      %setspeed
    [~ this]
    ::
      %tcdrain
    [~ this]
    ::
      %tcflow
    [~ this]
    ::
      %tcflush
    [~ this]
    ::
      %tcsendbreak
    [~ this]
    ::
      %rite
    ?+  sign-arvo  (on-arvo:default wire sign-arvo)
      [%loch %rote *]
      :-  ~
        %_  this
          write  (~(put by write) device tus.sign-arvo)
        ==
      ==
    ::
      %read
    ?+  sign-arvo  (on-arvo:default wire sign-arvo)
      [%loch %seen *]
      :-  ~
        %_  this
          read  (~(put by read) device [dat.sign-arvo tus.sign-arvo])
        ==
      ==
  ==
++  on-watch  on-watch:default
++  on-leave  on-leave:default
++  on-agent  on-agent:default
++  on-fail   on-fail:default
--
