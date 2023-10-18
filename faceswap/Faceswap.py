import os
import cv2
import insightface
from insightface.app import FaceAnalysis

if __name__ == '__main__':
    app = FaceAnalysis(name='buffalo_l')
    app.prepare(ctx_id=0, det_size=(640, 640))
    swapper = insightface.model_zoo.get_model('inswapper_128.onnx', download=True, download_zip=True,
                                              providers=["CUDAExecutionProvider"])
    source_pos = 0
    face_imgs = os.listdir("faces")
    img = cv2.imread(os.path.join("faces", face_imgs[source_pos]))
    faces = app.get(img)
    faces = sorted(faces, key=lambda x: x.bbox[0])
    source_face = faces[0]


    showing_swap = False
    cap = cv2.VideoCapture(0)
    while cap.isOpened():
        ret, frame = cap.read()
        if frame is None:
            break
        faces = app.get(frame)
        if len(faces) == 0:
            continue
        face = faces[0]
        if showing_swap:
            res = swapper.get(frame, face, source_face, paste_back=True)
            cv2.imshow("", res)
            key = cv2.waitKey(1)
        else:

            cv2.imshow("", frame)
            key = cv2.waitKey(1)
        if key == ord("v") and showing_swap:
            source_pos += 1
            if source_pos >= len(face_imgs):
                source_pos = 0
            img = cv2.imread(os.path.join("faces", face_imgs[source_pos]))
            source_face_objs = app.get(img)
            source_face_objs = sorted(source_face_objs, key=lambda x: x.bbox[0])
            source_face = source_face_objs[0]

        if key == ord("s"):
            showing_swap = not showing_swap
