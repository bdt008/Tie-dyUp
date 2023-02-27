
//constants
const GET_ALL_STORE_REVIEWS = 'GET_ALL_STORE_REVIEWS';
const SINGLE_REVIEW = 'GET_SINGLE_REVIEW';
const CREATE_REVIEW = 'CREATE_REVIEW';
const UPDATE_REVIEW = 'UPDATE_REVIEW';
const DELETE_REVIEW = 'DELETE_REVIEW';

const getStoreReviews = (reviews) => {
    return {
        type: GET_ALL_STORE_REVIEWS,
        reviews
    }
};

const getSingleReview = (review) => {
    return {
        type: SINGLE_REVIEW,
        review
    };
};

const addReview = (review) => {
    return {
        type: CREATE_REVIEW,
        review,
    }
};

const updateReview = (review, parentId) => {
    return {
        type: UPDATE_REVIEW,
        review,
        parentId
    }
};

const deleteReview = (reviewId) => {
    return {
        type: DELETE_REVIEW,
        reviewId
    }
};

//THUNKS

//Get reviews for store
export const getAllStoreReviews = (store_id) = async (dispatch) => {
    const res = await fetch(`/api/stores/${store_id}/reviews`);
    if (res.ok) {
        const data = await res.json();
        dispatch(getStoreReviews(data.Reviews))
    }
    return res;
}

//Get a single review
export const getReview = (reviewId) => async(dispatch) => {
    const res = await fetch(`/api/reviews/${reviewId}`)

    if(res.ok){
        const review =  await res.json();
        dispatch(getSingleReview(review))
    };
};

// create a review
export const createReview = (review) => async(dispatch) =>  {
    const {content, photo, star_rating} =  review;

    const res = await fetch(`/api/stores/${store_id}/reviews`, {
        method: 'POST',
        body: JSON.stringify({
            content,
            photo,
            star_rating
        })
    });

    if(res.ok){
        const data = await res.json();
        dispatch(addReview(data));
        return res
    }
};

//update a review
export const editReview = (review, reviewId, parentId) => async(dispatch) =>  {
    const {content} = review;
    const res = await fetch(`/api/reviews/${reviewId}`, {
        method: 'PUT',
        body: JSON.stringify({
          content
        }),
    });

    if(res.ok){
        const updatedReview = await res.json();
        dispatch(updateReview(updatedReview, parentId)); //parentId is used to update the parent object's state in the redux store
        return res
    }
};


//delete a review
export const deleteAReview = (reviewId) => async (dispatch) => {
    const res = await fetch(`/api/reviews/${reviewId}`, {
        method: 'DELETE'
    });
    const response = await res.json();
    if(res.status === 200){
        dispatch(deleteReview(reviewId));
    }
    return response;
};

//reducer
const initialState = {reviews: {}, replies: {}};

export default function reviewsReducer(state = initialState, action){
    let newState = {...state}
    switch(action.type){
        case  GET_ALL_STORE_REVIEWS:
            newState = {}
            action.reviews.forEach((review) => newState[review.id] = review);
            return newState
        case SINGLE_REVIEW:
            newState[action.review.id] = action.review;
            return newState;
        case CREATE_REVIEW:
            newState[action.review.id] = action.review
            return newState;
        case UPDATE_REVIEW:
            newState[action.review.id] = action.review;
            return  newState;
        case DELETE_REVIEW:
            delete newState[action.reviewId]
            return newState;
        default:
            return state;
        };
};
