---
title: Matrix Decomposition
created: '2013-04-24T23:14:16-07:00'
date: '2026-11-15T09:19:25-08:00'
authors:
  - bendu
label: matrix-decomposition
license: CC-BY-4.0
tags:
  - Statistics
  - math
  - algebra
  - decomposition
  - matrix
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## QR Decomposition

The QR decomposition uses the Gram-Schmidt process to express a set of vectors
(columns of design matrix from statistical view) in a set of orthogonal unit vecotors (which means that Q is matrix with orthogonal unit vectors)
so that for any `k`,
the space spanned by the first `k` original vectors is the same as the space spanned by the first `k` orthogonal unit vectors.
The ith column of R is the way that the ith original vector can be expressed in the first `i` orthogonal unit vectors.\
This means that R is an upper (right) triangular matrix.

More specifically,
For any real matrix $X_{n\times p}$, there $Q_{n\times p}$ and $R_{p\times p}$ such that
(X\_{n\\times p} = Q\_{n\\times p} R\_{p\\times p}),
where $Q$ is a matrix with orthogonal unit column vectors,
i.e., $Q'Q=I$; $R$ is an upper (right) triangular matrix.
QR decomposition is often done through Gram-Schmidt process.
Given a vector $x_i$,
the Gram-Schmidt process produce a (unit) vector $e_i$ that is orthogonal to previously produced orthogonal vectors $\{e_1,...,e_{i-1}\}$.
This is done by subtract the projection of $e_i$ to the space spanned by $\{e_1,...,e_{i-1}\}$ from $e_i$ (and then normalize it).
For any $i$,
the spaces spanned by $\{x_1, ..., x_i\}$ and $\{e_1, ..., e_i\}$ are the same.
The $i^{th}$ column of $R$ is the way that $x_i$ can be expressed by $\{e_1, ..., e_i\}$,
i.e., the first $i$ columns of $Q$.

QR decomposition can be used to

1. determine the rank of a matrix.
   For example, to find the rank of a matrix X in R, you can use command `qr(X)$rank`.

1. find estimates of coefficients in linear regression,
   which is
   (\\hat{\\beta} = R^\{-1}Q'\\boldsymbol\{y}).
   The fact that R is an upper (right) triangular matrix make it easy to find its inverse.

## Singular Value Decomposition

For any real matrix $X_{n\times p}$ of rank $r$,
there exists matrix $U_{n\times r}$, $D_{r\times r}$ and $V_{p\times r}$ such that
(X=UDV'),
where $U$ is a matrix with orthogonal unit column vectors spanning the column space of X;
$D$ is a diagonal matrix with positive (decreasing) diagonal elements;
$V$ is a matrix with orthogona unit row vectors spanning the row space of X.

1. If we expand $U$ and $V$ to be squared matrixes (adding 0's into the diagonal elements of $D$),
   the SVD can be explained as to use rotation, scaling and rotation to express any linear map $X$.

1. $X$ maps a unit sphere into a ellipsoid.
   The singular values are the semiaxes of the ellipsoid.

1. The singular values are square root of the eigenvalues of $X'X$ and $XX'$.

1. If $X$ is a square matrix and has eigenvalue decomposition,
   then the singular values are absolute eigenvalues of $X$.

1. If $X$ is a nonnegative definite matrix,
   then the SVD is the eigenvalue decomposition.

1. The SVD can be rewritten as a weighted (singular values are the weights) sum of separable matrixes.

The SVD can be used to

1. find the rank of the matrix $X$.

1. find pseudoinverse inverse of the matrix $X$.

1. find lower rank approximation of the matrix $X$.
   This is one way to reduce dimension in statistics.

## Eigendecomposition (Spectral Decomposition)

1. Only diagonalizable matrices have eigendecompostions.
   The geometric dimension of an eigenvalue of a matrix is less than or equal to its algebraic dimension.
   A matrix is diagonalizable iff the geometric dimension is the same as the algebraic dimension for each eigenvalue.
   Nonnegative definite matrices are diagonalizable.
   Specially project matrices are diagonalizable (with eigenvalues 0 and 1).

1. For a Markov chain process,
   a stationary distribution is an eigenvalue of the transition matrix with respect to the eigenvalue 1.

1. The eigendecomposition can be used to calculate the power of diagonalizable matrices.

1. Eigendecomposition is used in principal components analysis.
