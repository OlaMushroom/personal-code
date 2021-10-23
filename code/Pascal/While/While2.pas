program Tichso;
uses crt;
var i,tich:longint;N:integer;
begin
  clrscr;
  write('Nhap N = ');readln(N);
  tich:=1;i:=1;
  While i<=N do
  begin
    tich:=tich*i;i:=i+1;
  end;
  write('Tich N so nguyen dau tien la: ',tich);readln;
end.