(import 'java.util.Base64)

(def signature [0x89 0x50 0x4E 0x47 0x0D 0x0A 0x1A 0x0A])

(defn decode64 [s]
  (->> (.decode (Base64/getMimeDecoder) s)
       (map (comp #(mod % 256) (partial + 256)))))

;; From https://github.com/clojure/math.combinatorics
(defn cartesian-product [& seqs]
  (let [v-original-seqs (vec seqs)
        step
        (fn step [v-seqs]
          (let [increment
                (fn [v-seqs]
                  (loop [i (dec (count v-seqs)), v-seqs v-seqs]
                    (if (= i -1) nil
                      (if-let [rst (next (v-seqs i))]
                        (assoc v-seqs i rst)
                        (recur (dec i) (assoc v-seqs i (v-original-seqs i)))))))]
            (when v-seqs
              (cons (map first v-seqs)
                    (lazy-seq (step (increment v-seqs)))))))]
    (when (every? seq seqs)
      (lazy-seq (step v-original-seqs)))))

(defn decode [img key]
  (map bit-xor (cycle key) img))

(defn matches? [img key]
  (= signature (decode (take 8 img) key)))

(defn get-key [img]
  (let [alphabet (map (partial + 97) (range 26))
        keys ((fn ! [n] (lazy-cat (->> alphabet (repeat n)
                                      (apply cartesian-product))
                          (! (inc n)))) 1)]
    (->> (filter (partial matches? img) keys) first)))

(let [img (decode64 (slurp *in*))
      key (get-key img)]
  (println (apply str (map char key)))
  (with-open [w (clojure.java.io/output-stream "out.png")]
    (.write w (byte-array (decode img key)))))
