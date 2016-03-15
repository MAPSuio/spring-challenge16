(require r5rs)

(define (cycle lst)
  (define (iter l)
    (if (null? (cdr l))
        (set-cdr! l lst)
        (iter (cdr l))))
  (iter lst) lst)

(define (cards n)
  (define (iter n res)
    (if (zero? n)
        res
        (iter (- n 1) (cons n res))))
  (iter n '()))

(define (filter pred lst)
  (cond ((null? lst) '())
        ((pred (car lst))
         (cons (car lst) (filter pred (cdr lst))))
        (else (filter pred (cdr lst)))))

(define (qs lst key)
  (if (null? lst)
      lst
      (append
       (qs (filter (lambda (x) (<= (key x) (key (car lst)))) (cdr lst)) key)
       (list (car lst))
       (qs (filter (lambda (x) (> (key x) (key (car lst)))) (cdr lst)) key))))

(define (sorting-dimonds n)
  (define (iter c res)
    (if (eq? c (cdr c))
        (cons (car c) res)
        (let ((e (cadr c)))
          (set-cdr! c (cddr c))
          (iter (cdr c) (cons e res)))))
  (let* ((deck (cycle (cons n (cards (- n 1)))))
         (pairs (map (lambda (x y) (cons x y))
                     (reverse (iter deck '()))
                     (cards n))))
    (map cdr (qs pairs car))))
