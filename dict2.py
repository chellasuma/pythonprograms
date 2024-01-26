a={'a':'abc',1:1234,'b':'bcde',2:2345}
out={a[i]:i  for i in  a if isinstance(a[i],str)}
print(out)/