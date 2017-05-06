package fr.extragornax.drunktest;

import android.content.Intent;
import android.os.Bundle;
import android.provider.ContactsContract;
import android.app.ListActivity;
import android.database.Cursor;
import android.view.View;
import android.widget.ListView;
import android.widget.SimpleCursorAdapter;

public class ContactPage extends ListActivity {


    @Override
    public long getSelectedItemId() {
        // TODO Auto-generated method stub
        return super.getSelectedItemId();
    }

    @Override
    public int getSelectedItemPosition() {
        // TODO Auto-generated method stub
        return super.getSelectedItemPosition();
    }

    ListView lv;
    Cursor cursor1;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.contact);

        // create a cursor to query the Contacts on the device to start populating a listview
        cursor1 = getContentResolver().query(ContactsContract.CommonDataKinds.Phone.CONTENT_URI, null, null, null, null);
        startManagingCursor(cursor1);

        // get the list items for the listadapter could be TITLE or URI
        String[] from = {ContactsContract.CommonDataKinds.Phone.DISPLAY_NAME, ContactsContract.CommonDataKinds.Phone.NUMBER, ContactsContract.CommonDataKinds.Phone._ID};


        int[] to = {android.R.id.text1, android.R.id.text2}; // sets the items from above string to listview

        // new listadapter, created to use android checked template
        SimpleCursorAdapter listadapter = new SimpleCursorAdapter(this, android.R.layout.simple_list_item_2, cursor1, from, to);


        setListAdapter(listadapter);

        // adds listview so I can get data from it
        lv = getListView();
        lv.setChoiceMode(ListView.CHOICE_MODE_MULTIPLE);

    }

    public void openText(View view){
        finish();
    }

}