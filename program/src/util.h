void dotProduct(float* ptr_veca, float* ptr_vecb, float* ptr_result, int dim);

/*
 * computes the norm (length) of a vector pointed to by `ptr_vec`.
 *
 * Norm of a vector x = || x || = sqrt(dotProduct(x, x))
 *
 */
float norm(float* ptr_vec, int dim);

/*
 * b = 1/2 * (||c_-||^2 - ||c_+||^2)
 *
 * This is the most simple computation for the b component of wx + b = 0
 */
float getB(float c_positive, float c_negative);

/*
 * x = [1, 2, 3];
 *
 * sum(x) = 6
 *
 * Sums up one dimensional vector into a number as follows:
 *
 * s = sum(x[i]) for i = 0...len(x)
 */
float sumVector(float* ptr_vec, int dim);


