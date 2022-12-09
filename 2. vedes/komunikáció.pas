uses crt;

var f:file;
    i:longint;


begin clrscr;
    assign(f,'barmi.txt');
    reset(f);                  // fileMode = 2  olvasás és irási jog       rewrite(f) = csak irási

    while not(eof(f)) do begin                // eof = end of fileig olvas
        read(f,i)
        write(f,i+1)
    end;

    close(f)

end.