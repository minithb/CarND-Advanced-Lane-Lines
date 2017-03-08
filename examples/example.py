def warper(img, src, dst):

    # Compute and apply perpective transform
    img_size = (img.shape[1], img.shape[0])
    M = cv2.getPerspectiveTransform(src, dst)
    warped = cv2.warpPerspective(img, M, img_size, flags=cv2.INTER_NEAREST)  # keep same size as input image

    return warped


<select id="navtab" style="background-color:#E5E5E5;" class="select form-control"> <option value="0">Tickets <i aria-hidden="true" style="font-size:14px;float:right;" class="fa fa-chevron-down"></option> <option value="1">Description <i aria-hidden="true" style="font-size:14px;float:right;" class="fa fa-chevron-down"></option> <option value="2">Venue <i aria-hidden="true" style="font-size:14px;float:right;" class="fa fa-chevron-down"></option></select>