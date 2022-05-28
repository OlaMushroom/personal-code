Program Tong_1000;
uses crt;
var i,S:longint;
const N=1000;
begin
  clrscr;
  S:=0;
  while i<=N do
  begin
    S:=S+i;inc(i);
  end;
    writeln('Tong 1000 so nguyen dau tien la: ',S);readln;
end.