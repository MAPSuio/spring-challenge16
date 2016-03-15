(import 'java.util.Base64)

(def signature [0x89 0x50 0x4E 0x47 0x0D 0x0A 0x1A 0x0A])

(defn decode64 [s]
  (->> (.decode (Base64/getMimeDecoder) s)
       (map (comp #(mod % 256) (partial + 256)))))

(defn decode [img key]
  (map bit-xor key img))

(defn smallest-cycle [s]
  (let [keys (map #(take % s) (range 1 (count s)))]
    (-> (comp (partial = s) (partial take 8) cycle)
        (filter keys) first)))

(defn get-key [img]
  (smallest-cycle (decode signature img)))

(let [img (decode64 (slurp *in*))
      key (get-key img)]
  (println (apply str (map char key)))
  (with-open [w (clojure.java.io/output-stream "out.png")]
    (.write w (byte-array (decode img (cycle key))))))
