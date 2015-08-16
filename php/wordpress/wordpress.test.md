## ページアクセステスト


~~~php
<?php class SampleTest extends WP_UnitTestCase {

    /*  
     * phpunit --filter 'SampleTest::test_getpost'
    */
    function test_getpost(){
        $user_id = $this->factory->user->create();
        $post_id = $this->factory->post->create(
            array('post_author' => $user_id,
                  'post_title' => 'Post test',
                  'post_type' => 'page',
                  'post_status'  => 'publish')); 

        // TODO: MUST use `get_permalink` call,
        // which generate a url like `http://example.org/?page_id=3` , 
        // not `?p=3`.
        $url = get_permalink($post_id);

        // TODO: I don't know why this is blank.
        $this->assertEquals('', get_option('permalink_structure'));

        // Access the URL
        $this->go_to($url);
            
        global $wp_query;
        $post = $wp_query->get_queried_object();
        $this->assertEquals($post->ID, $post_id); 
        // or simpley
        $this->assertEquals(get_queried_object()->ID, $post_id); 
    }   
