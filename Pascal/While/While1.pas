Program Tong_n_so_nguyen;
uses crt;
Var i,n: integer;S:real;
begin
  write('Nhap so nguyen duong n: ');readln(n);
  S:=0;i:=1;
  while i<=n do
  begin
    S:=S+i;i:=i+1;
  end;
  writeln('Tong cua ',n,' so nguyen dau tien la ',S:10:2);readln;
end.