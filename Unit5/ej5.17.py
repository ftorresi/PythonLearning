import numpy as np

def write_table_to_file(f, xmin, xmax, nx, ymin, ymax, ny, width=10, decimals=None, filename="table.dat"):
    xval=np.linspace(xmin,xmax,nx+1)
    yval=np.linspace(ymax,ymin,ny+1)
    fval=np.zeros((ny+1, nx+1))
    
    #Make table
    for i in range(ny+1):
        for j in range(nx+1):
            fval[i,j]=f(xval[j],yval[i])
    
    #Output format
    if decimals==None:
        outformat="%%%gg" %width
    else:
        outformat="%%%g.%gg" %(width,decimals) 
    
    #Write table in file
    outfile=open(filename,"w")
    
    for i in range(ny+1):
        outfile.write(outformat %yval[i])
        for j in range(nx+1):
            outfile.write(outformat %fval[i,j])
        outfile.write("\n")
    spacestr=" "*width
    outfile.write("%s" %spacestr) #to align x values
    for j in range(nx+1):
        outfile.write(outformat %xval[j])
        
    outfile.close()
        
    
    
def test_write_table_to_file(): 
    filename = 'tmp.dat'
    write_table_to_file(f=lambda x, y: x + 2*y,
                        xmin=0, xmax=2, nx=4, ymin=-1,
                        ymax=2, ny=3,
                        width=5, decimals=None,
                        filename=filename)
    # Load text in file and compare with expected results
    with open(filename, 'r') as infile:
        computed = infile.read()
    expected = """\
    2    4  4.5    5  5.5    6
    1    2  2.5    3  3.5    4
    0    0  0.5    1  1.5    2
   -1   -2 -1.5   -1 -0.5    0
         0  0.5    1  1.5    2"""
    assert computed == expected

test_write_table_to_file()

write_table_to_file(f=lambda x, y: 0.5*x + 2*y, xmin=0, xmax=2, nx=8, ymin=-2, ymax=2, ny=8, width=8, decimals=4, filename="ej5.17-table.dat")
    
