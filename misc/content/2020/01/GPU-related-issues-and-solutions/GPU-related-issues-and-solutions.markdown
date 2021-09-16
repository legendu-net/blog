Status: published
Date: 2020-01-03 09:22:43
Author: Benjamin Du
Slug: GPU-related-issues-and-solutions
Title: GPU Related Issues and Solutions
Category: Computer Science
Tags: programming, GPU, issues, solutions
Modified: 2021-09-16 09:54:29

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**


## A Large Portion of GPU Memory is Already Used

If you train models using GPU on your own desktop computer
(no matter Linux or Windows),
you might notice that even before you do anything with model training,
there's already a large portion of GPU memory used by other applications
(check it using `nvidia-smi`).
It is suggested that you take the following actions to free GPU memories 
before training your models.

1. Close non-needed applications (especially those apps which uses GPU).

2. Switch to TTY (using the shortcut Ctrl + Shift + F1, F2, etc.) if you are using Linux,
    which can already help free most used GPU memories.

3. Boot your Linux machine into text model if you absolutely want squeeze all GPU memory 
    out of other applications (mostly X11).

## CUDA Out of Memory

torch.cuda.memory_summary()

[How to avoid "CUDA out of memory" in PyTorch](https://stackoverflow.com/questions/59129812/how-to-avoid-cuda-out-of-memory-in-pytorch)

1. reduce training/testing batch size

2. clear PyTorch caches

3. add `torch.cuda.empty_cache()` before training each epoch

4. Free GPU memory from other applications (see the previous section)

[OOM error where ~50% of the GPU RAM cannot be utilised/reserved #35901](https://github.com/pytorch/pytorch/issues/35901)

## ptxas application ptx input, line 9; fatal   : Unsupported .version 6.5; current version is '6.4'

After installing cudatoolkit 10.2.89, 
I got the following error message when using the numba JIT feature.

> /home/admin1/anaconda3/lib/python3.7/site-packages/numba/cuda/decorators.py:111: UserWarning: autojit is deprecated and will be removed in a future release. Use jit instead.
>   warn('autojit is deprecated and will be removed in a future release. Use jit instead.')
> Traceback (most recent call last):
>   File "/home/admin1/anaconda3/lib/python3.7/site-packages/numba/cuda/cudadrv/driver.py", line 1563, in add_ptx
>     ptxbuf, len(ptx), namebuf, 0, None, None)
>   File "/home/admin1/anaconda3/lib/python3.7/site-packages/numba/cuda/cudadrv/driver.py", line 288, in safe_cuda_api_call
>     self._check_error(fname, retcode)
>   File "/home/admin1/anaconda3/lib/python3.7/site-packages/numba/cuda/cudadrv/driver.py", line 323, in _check_error
>     raise CudaAPIError(retcode, msg)
> numba.cuda.cudadrv.driver.CudaAPIError: [218] Call to cuLinkAddData results in UNKNOWN_CUDA_ERROR
> 
> During handling of the above exception, another exception occurred:
> 
> Traceback (most recent call last):
>   File "./test.py", line 28, in <module>
>     func2(a)
>   File "/home/admin1/anaconda3/lib/python3.7/site-packages/numba/cuda/dispatcher.py", line 42, in __call__
>     return self.compiled(*args, **kws)
>   File "/home/admin1/anaconda3/lib/python3.7/site-packages/numba/cuda/compiler.py", line 736, in __call__
>     kernel = self.specialize(*args)
>   File "/home/admin1/anaconda3/lib/python3.7/site-packages/numba/cuda/compiler.py", line 747, in specialize
>     kernel = self.compile(argtypes)
>   File "/home/admin1/anaconda3/lib/python3.7/site-packages/numba/cuda/compiler.py", line 765, in compile
>     kernel.bind()
>   File "/home/admin1/anaconda3/lib/python3.7/site-packages/numba/cuda/compiler.py", line 495, in bind
>     self._func.get()
>   File "/home/admin1/anaconda3/lib/python3.7/site-packages/numba/cuda/compiler.py", line 377, in get
>     linker.add_ptx(ptx)
>   File "/home/admin1/anaconda3/lib/python3.7/site-packages/numba/cuda/cudadrv/driver.py", line 1565, in add_ptx
>     raise LinkerError("%s\n%s" % (e, self.error_log))
> numba.cuda.cudadrv.driver.LinkerError: [218] Call to cuLinkAddData results in UNKNOWN_CUDA_ERROR
> ptxas application ptx input, line 9; fatal   : Unsupported .version 6.5; current version is '6.4'
> ptxas fatal   : Ptx assembly aborted due to errors

Downgrading cudatoolkit to 10.1.243 fixed the issue.
