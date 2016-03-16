(declare solutions)

(def pmapcat (comp (partial apply concat) pmap))

(defn check [n v]
  (let [y (+ (v (- n 2)) (v 0))]
    (when (and ((complement (set v)) y) (< y n))
      (list (assoc v (dec n) y)))))

(defn generate [n v]
  (let [m (-> (take-nth 2 v) (.indexOf nil) (* 2))
        xs (filter (complement (set v)) (range 1 (dec n)))]
    (mapcat (fn [x]
              (let [y (+ x (v (- m 2)))]
                (when (and ((complement (set v)) y) (< y n))
                  (-> v (assoc m x) (assoc (dec m) y) solutions))))
            xs)))

(defn solutions [v]
  (let [n (count v)]
    (if (every? identity (take-nth 2 v))
      (check n v)
      (generate n v))))

(defn solve [n]
  (and (mod n 2)
       (pmapcat #(solutions (into [(- n %) n %] (repeat (- n 3) nil)))
                (range 2 (/ n 2)))))

(->> 20 solve count println)
