#lang racket
(define (greatest_common_factor a b)
  
  (define (gcf-iter a b)
    (if (not (= b 0))
        (gcf-iter b (modulo a b))
        a))
  
  (gcf-iter a b))

(greatest_common_factor 8 16)