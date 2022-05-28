Program Tong_A;
uses crt;
var i,N:integer;S:real;
begin
  clrscr;
  i:=2;S:=0;
  write('Nhap N = ');readln(N);
  while i<=N do
  begin
    S:=S+1/i;i:=i+1;
  end;
  writeln('Tong A la: ',S:6:2);readln;
end.