# pyflann
Research NN searching method FLANN

## Compule flann by yourself

1. download source code 
2. make sure install the following packages:
	cmake
    libhdf5-dev
    libgtest-dev :这个库最好是自己下载只有进行自己编译，这个编译过程比较好
    mpi 和mp等库
3. update CMakeList.txt
	for example: I haven't install matlab in my machine 
and I set the Matlab bind from **ON** to **OFF**.
4. cmake ..  
   sudo make all
   NOTE: make process may have a long time in virtul machine, and the process may
be halt in somewhere, please wait...
   sudo make install

## FLANN库
[Flann 参考手册](http://www.cs.ubc.ca/research/flann/uploads/FLANN/flann_manual-1.8.4.pdf)
Muja, M., & Lowe, D. G. (2014). Scalable nearest neighbor algorithms for high dimensional data. IEEE Transactions on Pattern Analysis & Machine Intelligence, 36(11), 2227-2240.
FLANN库全称是Fast Library for Approximate Nearest Neighbors，它是目前最完整的（近似）最近邻开源库。不但实现了一系列查找算法，还包含了一种自动选取最快算法的机制。